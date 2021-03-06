import unittest
import unittest.mock

import relations.sql

class TestSQL(unittest.TestCase):

    def test_delimit_clause(self):

        self.assertEqual(relations.sql.delimit_clause({"a": 1, "b": 2}, ",", ":", reverse=True), "1:a,2:b")
        self.assertEqual(relations.sql.delimit_clause({"a": 1, "b": 2}, ",", ":"), "a:1,b:2")
        self.assertEqual(relations.sql.delimit_clause(["a:1", "b:2"], ",", ":"), "a:1,b:2")
        self.assertEqual(relations.sql.delimit_clause([1, 2], ",", ":"), "1,2")
        self.assertEqual(relations.sql.delimit_clause("a:1,b:2", ",", ":"), "a:1,b:2")

    def test_as_clause(self):

        self.assertEqual(relations.sql.as_clause({"a": 1, "b": 2}), "1 AS a,2 AS b")

    def test_equals_clause(self):

        self.assertEqual(relations.sql.equals_clause({"a": 1, "b": 2}), "a=1 AND b=2")

    def test_comma_clause(self):

        self.assertEqual(relations.sql.comma_clause({"a": 1, "b": 2}), "a,1,b,2")

    def test_assign_clause(self):

        self.assertEqual(relations.sql.assign_clause({"a": 1, "b": 2}), "a=1,b=2")

    def test_options_clause(self):

        self.assertEqual(relations.sql.options_clause({"a": 1, "b": 2}), "a 1 b 2")

    def test_values_clause(self):

        self.assertEqual(relations.sql.values_clause([{"a": 1, "b": 2}, {"a": 3, "b": 4}]), "(a,b) VALUES (1,2),(3,4)")
        self.assertEqual(relations.sql.values_clause({"a": 1, "b": 2}), "(a,b) VALUES (1,2)")
        self.assertEqual(relations.sql.values_clause("(a,b) VALUES (1,2)"), "(a,b) VALUES (1,2)")

    def test_as_clause_add(self):

        self.assertEqual(relations.sql.as_clause_add("yes", {}), "yes")
        self.assertEqual(relations.sql.as_clause_add("yes", {"a": 1, "b": 2}), "yes,1 AS a,2 AS b")
        self.assertEqual(relations.sql.as_clause_add("", {"a": 1, "b": 2}), "1 AS a,2 AS b")

    def test_equals_clause_add(self):

        self.assertEqual(relations.sql.equals_clause_add("yes", {}), "yes")
        self.assertEqual(relations.sql.equals_clause_add("yes", {"a": 1, "b": 2}), "yes AND a=1 AND b=2")
        self.assertEqual(relations.sql.equals_clause_add("", {"a": 1, "b": 2}), "a=1 AND b=2")

    def test_comma_clause_add(self):

        self.assertEqual(relations.sql.comma_clause_add("yes", {}), "yes")
        self.assertEqual(relations.sql.comma_clause_add("yes", {"a": 1, "b": 2}), "yes,a,1,b,2")
        self.assertEqual(relations.sql.comma_clause_add("", {"a": 1, "b": 2}), "a,1,b,2")

    def test_assign_clause_add(self):

        self.assertEqual(relations.sql.assign_clause_add("yes", {}), "yes")
        self.assertEqual(relations.sql.assign_clause_add("yes", {"a": 1, "b": 2}), "yes,a=1,b=2")
        self.assertEqual(relations.sql.assign_clause_add("", {"a": 1, "b": 2}), "a=1,b=2")

    def test_options_clause_add(self):

        self.assertEqual(relations.sql.options_clause_add("yes", {}), "yes")
        self.assertEqual(relations.sql.options_clause_add("yes", {"a": 1, "b": 2}), "yes a 1 b 2")
        self.assertEqual(relations.sql.options_clause_add("", {"a": 1, "b": 2}), "a 1 b 2")

    def test_as_clause_set(self):

        self.assertEqual(relations.sql.as_clause_set("yes", {}), "yes")
        self.assertEqual(relations.sql.as_clause_set("yes", {"a": 1, "b": 2}), "1 AS a,2 AS b")

    def test_equals_clause_set(self):

        self.assertEqual(relations.sql.equals_clause_set("yes", {}), "yes")
        self.assertEqual(relations.sql.equals_clause_set("yes", {"a": 1, "b": 2}), "a=1 AND b=2")

    def test_comma_clause_set(self):

        self.assertEqual(relations.sql.comma_clause_set("yes", {}), "yes")
        self.assertEqual(relations.sql.comma_clause_set("yes", {"a": 1, "b": 2}), "a,1,b,2")

    def test_assign_clause_set(self):

        self.assertEqual(relations.sql.assign_clause_set("yes", {}), "yes")
        self.assertEqual(relations.sql.assign_clause_set("yes", {"a": 1, "b": 2}), "a=1,b=2")

    def test_options_clause_set(self):

        self.assertEqual(relations.sql.options_clause_set("yes", {}), "yes")
        self.assertEqual(relations.sql.options_clause_set("yes", {"a": 1, "b": 2}), "a 1 b 2")

    def test_ensure_list(self):

        self.assertEqual(relations.sql.ensure_list(["a", "b"], " and "), ["a", "b"])
        self.assertEqual(relations.sql.ensure_list("a and b", " and "), ["a", "b"])
        self.assertEqual(relations.sql.ensure_list(None, " and "), [])

    def test_ensure_dict(self):

        self.assertEqual(relations.sql.ensure_dict({"a": True, "b": True}, " and "), {"a": True, "b": True})
        self.assertEqual(relations.sql.ensure_dict("a and b", " and "), {"a": True, "b": True})
        self.assertEqual(relations.sql.ensure_dict(["a", "b"], " and "), {"a": True, "b": True})
        self.assertEqual(relations.sql.ensure_dict(None, " and "), {})
